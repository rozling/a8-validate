import yaml
from a8_validate.schema_validator import PRESET_SCHEMA, CHANNEL_SCHEMA, ZONE_SCHEMA

def get_min_max_value(schema):
    if 'min' in schema and 'max' in schema:
        return schema['min'], schema['max']
    elif 'values' in schema:
        try:
            min_val = min(schema['values'])
            max_val = max(schema['values'])
            return min_val, max_val
        except TypeError:
            return None, None
    else:
        return None, None

def build_preset_values(schema, min_or_max='min'):
    preset = {}
    for param, param_schema in schema.items():
        min_val, max_val = get_min_max_value(param_schema)
        # Include required parameters even if no min/max
        if min_val is None and max_val is None:
            if param_schema.get('required', False):
                # Use placeholder for required string parameters
                if param == "XfadeACV":
                    value = "1A"
                elif param == "XfadeBCV":
                    value = "2A"
                elif param == "XfadeCCV":
                    value = "3A"
                elif param == "XfadeDCV":
                    value = "4A"
                elif param_schema['type'] in ('string', 'string_or_number'):
                    value = "ExampleValue"
                else:
                    # For other types, skip or set None
                    value = None
                preset[param] = value
            continue
        value = min_val if min_or_max == 'min' else max_val
        if param_schema['type'] == 'string_or_number':
            value = "ExampleName" if min_or_max == 'min' else "Z" * 10
        elif param_schema['type'] == 'string' and 'max_length' in param_schema:
            length = param_schema['max_length']
            value = "A" * length if min_or_max == 'max' else "A"
        preset[param] = value
    return preset

def build_channel_values(schema, min_or_max='min'):
    channel = {}
    for param, param_schema in schema.items():
        min_val, max_val = get_min_max_value(param_schema)
        if min_val is None and max_val is None:
            continue
        value = min_val if min_or_max == 'min' else max_val
        if param_schema['type'] == 'string_or_number':
            value = "ExampleName" if min_or_max == 'min' else "Z" * 10
        elif param_schema['type'] == 'string' and 'max_length' in param_schema:
            length = param_schema['max_length']
            value = "A" * length if min_or_max == 'max' else "A"
        channel[param] = value
    channel['Zone 1'] = build_zone_values(ZONE_SCHEMA, min_or_max)
    return channel

def build_zone_values(schema, min_or_max='min'):
    zone = {}
    for param, param_schema in schema.items():
        min_val, max_val = get_min_max_value(param_schema)
        # Include required parameters even if no min/max
        if min_val is None and max_val is None:
            if param_schema.get('required', False):
                # Use placeholder for required string parameters
                if param == "Sample":
                    value = "test.wav"
                elif param_schema['type'] in ('string', 'string_or_number'):
                    value = "ExampleValue"
                else:
                    value = None
                zone[param] = value
            continue
        value = min_val if min_or_max == 'min' else max_val
        if param_schema['type'] == 'string_or_number':
            value = "ExampleName" if min_or_max == 'min' else "Z" * 10
        elif param_schema['type'] == 'string' and 'max_length' in param_schema:
            length = param_schema['max_length']
            value = "A" * length if min_or_max == 'max' else "A"
        zone[param] = value

    # Add loop parameters if LoopMode is 2 (Start/Length)
    if 'LoopMode' in zone and zone['LoopMode'] == 2:
        if 'LoopStart' not in zone or zone['LoopStart'] is None:
            zone['LoopStart'] = 0 if min_or_max == 'min' else 100
        if 'LoopLength' not in zone or zone['LoopLength'] is None:
            zone['LoopLength'] = 4 if min_or_max == 'min' else 1000

    return zone

def build_full_preset(min_or_max='min'):
    preset = {}
    preset_name = "Preset 1"
    # Build preset-level parameters first
    preset_params = build_preset_values(PRESET_SCHEMA, min_or_max)
    # Build channel 1
    channel1 = build_channel_values(CHANNEL_SCHEMA, min_or_max)
    # Build channel 2 if needed for crossfade groups
    channels = {'Channel 1': channel1}
    # Insert Master channel if needed for Cycle or Link modes
    needs_master = False
    for ch in channels.values():
        if 'ChannelMode' in ch and ch['ChannelMode'] in (1, 3):  # Link or Cycle
            needs_master = True
            break
    if needs_master:
        master_channel = build_channel_values(CHANNEL_SCHEMA, min_or_max)
        master_channel['ChannelMode'] = 0  # Master
        # Shift existing channels up by 1
        new_channels = {'Channel 1': master_channel}
        for ch_name, ch_data in channels.items():
            # Extract channel number
            num = int(ch_name.split(' ')[1])
            new_channels[f'Channel {num + 1}'] = ch_data
        channels = new_channels
    if 'XfadeGroup' in channel1:
        channel2 = build_channel_values(CHANNEL_SCHEMA, min_or_max)
        channel2['XfadeGroup'] = channel1['XfadeGroup']
        channels['Channel 2'] = channel2
        # Add corresponding XfadeCV parameter to preset_params
        group = channel1['XfadeGroup']
        xfade_cvs = {
            'A': 'XfadeACV',
            'B': 'XfadeBCV',
            'C': 'XfadeCCV',
            'D': 'XfadeDCV',
        }
        xfade_cv_param = xfade_cvs.get(group)
        if xfade_cv_param and xfade_cv_param not in preset_params:
            # Assign a default valid value
            preset_params[xfade_cv_param] = '1A'  # or appropriate default per group
    preset[preset_name] = preset_params
    preset[preset_name].update(channels)
    return preset

def main():
    min_preset = build_full_preset('min')
    max_preset = build_full_preset('max')

    with open('preset_min_values.yml', 'w') as f:
        yaml.dump(min_preset, f, sort_keys=False)

    with open('preset_max_values.yml', 'w') as f:
        yaml.dump(max_preset, f, sort_keys=False)

    print("Generated 'preset_min_values.yml' and 'preset_max_values.yml' with min and max parameter values.")

if __name__ == "__main__":
    main()
