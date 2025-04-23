"""Schema validator module for Assimil8or preset files."""

import re


class SchemaValidationError(Exception):
    """Base exception for schema validation errors."""
    pass


class InvalidParameterError(SchemaValidationError):
    """Exception raised for invalid parameter names."""
    pass


class InvalidValueError(SchemaValidationError):
    """Exception raised for invalid parameter values."""
    pass


class MissingRequiredParameterError(SchemaValidationError):
    """Exception raised for missing required parameters."""
    pass


# Define schema for preset parameters
PRESET_SCHEMA = {
    "Name": {"type": "string", "required": True, "max_length": 47},
    "Data2asCV": {"type": "cv_input", "required": False},
    "XfadeACV": {"type": "cv_input", "required": False},
    "XfadeAWidth": {"type": "float", "required": False, "min": 0.01, "max": 10.0},
    "XfadeBCV": {"type": "cv_input", "required": False},
    "XfadeBWidth": {"type": "float", "required": False, "min": 0.01, "max": 10.0},
    "XfadeCCV": {"type": "cv_input", "required": False},
    "XfadeCWidth": {"type": "float", "required": False, "min": 0.01, "max": 10.0},
    "XfadeDCV": {"type": "cv_input", "required": False},
    "XfadeDWidth": {"type": "float", "required": False, "min": 0.01, "max": 10.0},
    "MidiSetup": {"type": "integer", "required": False, "min": 1, "max": 16},
}

# Define schema for channel parameters
CHANNEL_SCHEMA = {
    "ChannelMode": {"type": "integer", "required": False, "values": [0, 1, 2, 3]},
    "Pitch": {"type": "float", "required": False, "min": -96.0, "max": 60.0},
    "Level": {"type": "float", "required": False, "min": -90.0, "max": 6.0},
    "Pan": {"type": "float", "required": False, "min": -1.0, "max": 1.0},
    "MixLevel": {"type": "float", "required": False, "min": -90.0, "max": 6.0},
    "PlayMode": {"type": "integer", "required": False, "values": [0, 1]},
    "LoopMode": {"type": "integer", "required": False, "values": [0, 1, 2]},
    "Reverse": {"type": "integer", "required": False, "values": [0, 1]},
    "Attack": {"type": "float", "required": False, "min": 0.0, "max": 99.0},
    "Release": {"type": "float", "required": False, "min": 0.0, "max": 99.0},
    "Bits": {"type": "float", "required": False, "min": 1.0, "max": 32.0},
    "Aliasing": {"type": "integer", "required": False, "min": 0, "max": 100},
    "SpliceSmoothing": {"type": "integer", "required": False, "values": [0, 1]},
    "PitchCV": {"type": "cv_input_with_amount", "required": False},
    "LinFM": {"type": "cv_input_with_amount", "required": False},
    "PhaseCV": {"type": "cv_input_with_amount", "required": False},
    "PMSource": {"type": "pm_source", "required": False},
    "PMIndex": {"type": "float", "required": False, "min": 0.0, "max": 1.0},
    "PMIndexMod": {"type": "cv_input_with_amount", "required": False},
    "LoopStart": {"type": "integer", "required": False, "min": 0},
    "LoopLength": {"type": "float", "required": False, "min": 4.0},
    "LoopStartMod": {"type": "cv_input_with_amount", "required": False},
    "LoopLengthMod": {"type": "cv_input_with_amount", "required": False},
    "SampleStart": {"type": "integer", "required": False, "min": 0},
    "SampleEnd": {"type": "integer", "required": False, "min": 1},
    "SampleStartMod": {"type": "cv_input_with_amount", "required": False},
    "SampleEndMod": {"type": "cv_input_with_amount", "required": False},
    "MixMod": {"type": "cv_input_with_amount", "required": False},
    "MixModIsFader": {"type": "integer", "required": False, "values": [0, 1]},
    "BitsMod": {"type": "cv_input_with_amount", "required": False},
    "AliasingMod": {"type": "cv_input_with_amount", "required": False},
    "AttackMod": {"type": "cv_input_with_amount", "required": False},
    "ReleaseMod": {"type": "cv_input_with_amount", "required": False},
    "ZonesCV": {"type": "cv_input", "required": False},
    "ZonesRT": {"type": "integer", "required": False, "values": [0, 1]},
    "XfadeGroup": {"type": "string", "required": False, "values": ["A", "B", "C", "D"]},
}

# Define schema for zone parameters
ZONE_SCHEMA = {
    "Sample": {"type": "string", "required": True},
    "MinVoltage": {"type": "voltage", "required": False, "min": -5.0, "max": 5.0},
    "MaxVoltage": {"type": "voltage", "required": False, "min": -5.0, "max": 5.0},
    "LevelOffset": {"type": "float", "required": False, "min": -90.0, "max": 6.0},
    "PitchOffset": {"type": "float", "required": False, "min": -96.0, "max": 60.0},
    "Side": {"type": "integer", "required": False, "values": [0, 1]},
    "LoopMode": {"type": "integer", "required": False, "values": [0, 1, 2]},
    "LoopStart": {"type": "integer", "required": False, "min": 0},
    "LoopLength": {"type": "float", "required": False, "min": 4.0},
    "SampleStart": {"type": "integer", "required": False, "min": 0},
    "SampleEnd": {"type": "integer", "required": False, "min": 1},
    "Bits": {"type": "float", "required": False, "min": 1.0, "max": 32.0},
    "Smooth": {"type": "integer", "required": False, "values": [0, 1]},
}

# Regex patterns for validation
CV_INPUT_PATTERN = r'^(Off|[0-8][A-C])$'
CV_INPUT_WITH_AMOUNT_PATTERN = r'^(Off|[0-8][A-C]) [-+]?[0-9]*\.?[0-9]+$'
VOLTAGE_PATTERN = r'^[-+]?[0-9]*\.?[0-9]+$'
PM_SOURCE_PATTERN = r'^([1-8]|Sample Input (Left|Right))$'


def validate_preset(preset_data):
    """
    Validate a preset against the schema.
    
    Args:
        preset_data: Dictionary containing the preset data
        
    Raises:
        SchemaValidationError: If validation fails
    """
    for preset_key, preset_value in preset_data.items():
        if not preset_key.startswith('Preset '):
            raise InvalidParameterError(f"Invalid preset key: {preset_key}")
        
        # Validate preset parameters
        for param, value in preset_value.items():
            if param.startswith('Channel '):
                # Validate channel
                channel_number = int(param.split(' ')[1])
                validate_channel(value, channel_number)
            else:
                # Validate preset parameter
                if param not in PRESET_SCHEMA:
                    raise InvalidParameterError(f"Invalid preset parameter: {param}")
                
                _validate_parameter_value(param, value, PRESET_SCHEMA[param])
        
        # Check for required parameters
        for param, schema in PRESET_SCHEMA.items():
            if schema.get('required', False) and param not in preset_value:
                raise MissingRequiredParameterError(f"Missing required preset parameter: {param}")


def validate_channel(channel_data, channel_number):
    """
    Validate a channel against the schema.
    
    Args:
        channel_data: Dictionary containing the channel data
        channel_number: Channel number
        
    Raises:
        SchemaValidationError: If validation fails
    """
    # Validate channel parameters
    for param, value in list(channel_data.items()):
        if param.startswith('Zone '):
            # Validate zone
            zone_number = int(param.split(' ')[1])
            validate_zone(value, channel_number, zone_number)
        else:
            # Validate channel parameter
            if param not in CHANNEL_SCHEMA:
                raise InvalidParameterError(f"Invalid channel parameter: {param} in Channel {channel_number}")
            
            _validate_parameter_value(param, value, CHANNEL_SCHEMA[param], f"Channel {channel_number}")


def validate_zone(zone_data, channel_number, zone_number):
    """
    Validate a zone against the schema.
    
    Args:
        zone_data: Dictionary containing the zone data
        channel_number: Channel number
        zone_number: Zone number
        
    Raises:
        SchemaValidationError: If validation fails
    """
    # Validate zone parameters
    for param, value in zone_data.items():
        if param not in ZONE_SCHEMA:
            raise InvalidParameterError(
                f"Invalid zone parameter: {param} in Channel {channel_number}, Zone {zone_number}"
            )
        
        _validate_parameter_value(
            param, value, ZONE_SCHEMA[param], f"Channel {channel_number}, Zone {zone_number}"
        )
    
    # Check for required parameters
    for param, schema in ZONE_SCHEMA.items():
        if schema.get('required', False) and param not in zone_data:
            raise MissingRequiredParameterError(
                f"Missing required zone parameter: {param} in Channel {channel_number}, Zone {zone_number}"
            )


def _validate_parameter_value(param, value, schema, context=""):
    """
    Validate a parameter value against its schema.
    
    Args:
        param: Parameter name
        value: Parameter value
        schema: Schema for the parameter
        context: Context for error messages (e.g., "Channel 1, Zone 2")
        
    Raises:
        SchemaValidationError: If validation fails
    """
    param_type = schema['type']
    context_str = f" in {context}" if context else ""
    
    # Type validation
    if param_type == 'string':
        if not isinstance(value, str):
            raise InvalidValueError(
                f"Parameter {param}{context_str} must be a string, got {type(value).__name__}"
            )
        if 'max_length' in schema and len(value) > schema['max_length']:
            raise InvalidValueError(
                f"Parameter {param}{context_str} exceeds maximum length of {schema['max_length']}"
            )
        if 'values' in schema and value not in schema['values']:
            raise InvalidValueError(
                f"Parameter {param}{context_str} must be one of {schema['values']}, got {value}"
            )
    
    elif param_type == 'integer':
        if not isinstance(value, int):
            raise InvalidValueError(
                f"Parameter {param}{context_str} must be an integer, got {type(value).__name__}"
            )
        if 'min' in schema and value < schema['min']:
            raise InvalidValueError(
                f"Parameter {param}{context_str} must be at least {schema['min']}, got {value}"
            )
        if 'max' in schema and value > schema['max']:
            raise InvalidValueError(
                f"Parameter {param}{context_str} must be at most {schema['max']}, got {value} (outside allowed range)"
            )
        if 'values' in schema and value not in schema['values']:
            raise InvalidValueError(
                f"Parameter {param}{context_str} must be one of {schema['values']}, got {value}"
            )
    
    elif param_type == 'float':
        if not isinstance(value, (int, float)):
            raise InvalidValueError(
                f"Parameter {param}{context_str} must be a float, got {type(value).__name__}"
            )
        if 'min' in schema and value < schema['min']:
            raise InvalidValueError(
                f"Parameter {param}{context_str} must be at least {schema['min']}, got {value} (outside allowed range)"
            )
        if 'max' in schema and value > schema['max']:
            raise InvalidValueError(
                f"Parameter {param}{context_str} must be at most {schema['max']}, got {value} (outside allowed range)"
            )
    
    elif param_type == 'cv_input':
        if not isinstance(value, str):
            raise InvalidValueError(
                f"Parameter {param}{context_str} must be a string, got {type(value).__name__}"
            )
        if not re.match(CV_INPUT_PATTERN, value):
            raise InvalidValueError(
                f"Parameter {param}{context_str} must be in format '1A'-'8C' or 'Off', got {value}"
            )
    
    elif param_type == 'cv_input_with_amount':
        if not isinstance(value, str):
            raise InvalidValueError(
                f"Parameter {param}{context_str} must be a string, got {type(value).__name__}"
            )
        if not re.match(CV_INPUT_WITH_AMOUNT_PATTERN, value):
            raise InvalidValueError(
                f"Parameter {param}{context_str} must be in format '1A 0.50', got {value}"
            )
    
    elif param_type == 'voltage':
        if not isinstance(value, str) and not isinstance(value, (int, float)):
            raise InvalidValueError(
                f"Parameter {param}{context_str} must be a number or string, got {type(value).__name__}"
            )
        
        # Convert to string if it's a number
        if isinstance(value, (int, float)):
            value = str(value)
        
        if not re.match(VOLTAGE_PATTERN, value):
            raise InvalidValueError(
                f"Parameter {param}{context_str} must be in format '+5.00' or '-3.50', got {value}"
            )
        
        # Check range
        try:
            float_val = float(value)
            if 'min' in schema and float_val < schema['min']:
                raise InvalidValueError(
                    f"Parameter {param}{context_str} must be at least {schema['min']}, got {value} (outside allowed range)"
                )
            if 'max' in schema and float_val > schema['max']:
                raise InvalidValueError(
                    f"Parameter {param}{context_str} must be at most {schema['max']}, got {value} (outside allowed range)"
                )
        except ValueError:
            raise InvalidValueError(
                f"Parameter {param}{context_str} must be a valid numeric value, got {value}"
            )
    
    elif param_type == 'pm_source':
        if isinstance(value, int) and 1 <= value <= 8:
            return
        
        if isinstance(value, str):
            if value in ['Sample Input Left', 'Sample Input Right']:
                return
            if value.isdigit() and 1 <= int(value) <= 8:
                return
        
        raise InvalidValueError(
            f"Parameter {param}{context_str} must be a channel number (1-8) "
            f"or 'Sample Input Left/Right', got {value}"
        )
