import yaml

from a8_validate.schema_validator import CHANNEL_SCHEMA, PRESET_SCHEMA, ZONE_SCHEMA


def get_min_max_value(schema):
    if "min" in schema and "max" in schema:
        return schema["min"], schema["max"]
    elif "values" in schema:
        try:
            min_val = min(schema["values"])
            max_val = max(schema["values"])
            return min_val, max_val
        except TypeError:
            return None, None
    else:
        return None, None


def build_preset_values(schema, min_or_max="min"):
    preset = {}
    for param, param_schema in schema.items():
        min_val, max_val = get_min_max_value(param_schema)
        if min_val is not None and max_val is not None:
            if min_or_max == "min":
                preset[param] = min_val
            else:
                preset[param] = max_val
        elif "values" in param_schema:
            # For enum types, use first or last value
            if min_or_max == "min":
                preset[param] = param_schema["values"][0]
            else:
                preset[param] = param_schema["values"][-1]
    return preset


def build_channel_values(schema, min_or_max="min"):
    channel = {}
    for param, param_schema in schema.items():
        if param.startswith("Zone "):
            continue  # Skip zone parameters at channel level
        min_val, max_val = get_min_max_value(param_schema)
        if min_val is not None and max_val is not None:
            if min_or_max == "min":
                channel[param] = min_val
            else:
                channel[param] = max_val
        elif "values" in param_schema:
            if min_or_max == "min":
                channel[param] = param_schema["values"][0]
            else:
                channel[param] = param_schema["values"][-1]
    return channel


def build_zone_values(schema, min_or_max="min"):
    zone = {}
    for param, param_schema in schema.items():
        min_val, max_val = get_min_max_value(param_schema)
        if min_val is not None and max_val is not None:
            if min_or_max == "min":
                zone[param] = min_val
            else:
                zone[param] = max_val
        elif "values" in param_schema:
            if min_or_max == "min":
                zone[param] = param_schema["values"][0]
            else:
                zone[param] = param_schema["values"][-1]
    return zone


if __name__ == "__main__":
    # Generate min values
    min_preset = build_preset_values(PRESET_SCHEMA, "min")
    min_channel = build_channel_values(CHANNEL_SCHEMA, "min")
    min_zone = build_zone_values(ZONE_SCHEMA, "min")

    min_preset["Channel 1"] = min_channel
    min_preset["Channel 1"]["Zone 1"] = min_zone

    with open("preset_min_values.yml", "w") as f:
        yaml.dump(
            {"Preset 1": min_preset}, f, default_flow_style=False, sort_keys=False
        )

    print("Generated preset_min_values.yml")

    # Generate max values
    max_preset = build_preset_values(PRESET_SCHEMA, "max")
    max_channel = build_channel_values(CHANNEL_SCHEMA, "max")
    max_zone = build_zone_values(ZONE_SCHEMA, "max")

    max_preset["Channel 1"] = max_channel
    max_preset["Channel 1"]["Zone 1"] = max_zone

    with open("preset_max_values.yml", "w") as f:
        yaml.dump(
            {"Preset 1": max_preset}, f, default_flow_style=False, sort_keys=False
        )

    print("Generated preset_max_values.yml")
