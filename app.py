import streamlit as st

st.title("Unit Converter")

conversion_types = [
    "Area", "Data Transfer Rate", "Digital Storage", "Energy", "Frequency",
    "Fuel Economy", "Length", "Mass", "Plane Angle", "Pressure", "Speed",
    "Temperature", "Time", "Volume"
]

# Unit dictionaries
unit_maps = {
    "Area": {
        "Square Kilometer": 1000000,
        "Square Meter": 1,
        "Square Mile": 2589988.11,
        "Square Yard": 0.836127,
        "Square Foot": 0.092903,
        "Square Inch": 0.00064516,
        "Hectare": 10000,
        "Acre": 4046.86,
    },
    "Data Transfer Rate": {
        "Bit per second": 1,
        "Kilobit per second": 1e3,
        "Megabit per second": 1e6,
        "Gigabit per second": 1e9,
        "Terabit per second": 1e12,
        "Kilobyte per second": 8e3,
        "Megabyte per second": 8e6,
        "Gigabyte per second": 8e9,
        "Terabyte per second": 8e12,
    },
    "Digital Storage": {
        "Bit": 1,
        "Kilobit": 1e3,
        "Megabit": 1e6,
        "Gigabit": 1e9,
        "Terabit": 1e12,
        "Byte": 8,
        "Kilobyte": 8e3,
        "Megabyte": 8e6,
        "Gigabyte": 8e9,
        "Terabyte": 8e12,
    },
    "Energy": {
        "Joule": 1,
        "Kilojoule": 1000,
        "Calorie": 4.184,
        "Kilocalorie": 4184,
        "Watt-hour": 3600,
        "Kilowatt-hour": 3600000,
        "British Thermal Unit": 1055.06,
        "Therm": 105505000,
    },
    "Frequency": {
        "Hertz": 1,
        "Kilohertz": 1e3,
        "Megahertz": 1e6,
        "Gigahertz": 1e9,
    },
    "Fuel Economy": {
        "Miles per gallon (US)": 1,
        "Kilometers per liter": 2.35215,
        "Liters per 100 kilometers": 235.215,
        "Miles per gallon (UK)": 1.20095,
    },
    "Length": {
        "Millimeter": 0.001,
        "Centimeter": 0.01,
        "Meter": 1,
        "Kilometer": 1000,
        "Inch": 0.0254,
        "Foot": 0.3048,
        "Yard": 0.9144,
        "Mile": 1609.34,
        "Nautical Mile": 1852,
        "Micrometer": 1e-6,
        "Nanometer": 1e-9,
    },
    "Mass": {
        "Milligram": 1e-6,
        "Gram": 0.001,
        "Kilogram": 1,
        "Microgram": 1e-9,
        "Pound": 0.453592,
        "Ounce": 0.0283495,
        "Stone": 6.35029,
        "Imperial Ton": 1016.05,
        "Us Ton": 907.185,
        "Tonne": 1000,
    },
    "Plane Angle": {
        "Degree": 1,
        "Radian": 57.2958,
        "Gradian": 0.9,
        "Minute of Arc": 0.0166667,
        "Second of Arc": 0.000277778,
        "Milliradian": 0.0572958,
    },
    "Pressure": {
        "Pascal": 1,
        "Bar": 1e5,
        "Standard Atmosphere": 101325,
        "Torr": 133.322,
        "Pound per square inch": 6894.76,
    },
    "Speed": {
        "Meter per second": 1,
        "Kilometer per hour": 0.277778,
        "Miles per hour": 0.44704,
        "Foot per second": 0.3048,
        "Knot": 0.514444,
    },
    "Temperature": {},  # Handled separately
    "Time": {
        "Nanosecond": 1e-9,
        "Microsecond": 1e-6,
        "Millisecond": 1e-3,
        "Second": 1,
        "Minute": 60,
        "Hour": 3600,
        "Day": 86400,
        "Week": 604800,
        "Month": 2592000,
        "Calendar year": 31536000,
        "Decade": 315360000,
        "Century": 3153600000,
    },
    "Volume": {
        "Milliliter": 0.001,
        "Liter": 1,
        "Cubic meter": 1000,
        "Cubic inch": 0.0163871,
        "Cubic foot": 28.3168,
        "US liquid gallon": 3.78541,
        "US liquid quart": 0.946353,
        "US liquid pint": 0.473176,
        "US fluid ounce": 0.0295735,
        "US tablespoon": 0.0147868,
        "US teaspoon": 0.00492892,
        "US legal cup": 0.236588,
        "Imperial gallon": 4.54609,
        "Imperial quart": 1.13652,
        "Imperial pint": 0.568261,
        "Imperial fluid ounce": 0.0284131,
        "Imperial tablespoon": 0.0177582,
        "Imperial teaspoon": 0.00591939,
        "Imperial cup": 0.284131,
    }
}

def convert(value, from_unit, to_unit, category):
    if category == "Temperature":
        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                return value * 9/5 + 32
            elif to_unit == "Kelvin":
                return value + 273.15
            else:
                return value
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                return (value - 32) * 5/9
            elif to_unit == "Kelvin":
                return (value - 32) * 5/9 + 273.15
            else:
                return value
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                return value - 273.15
            elif to_unit == "Fahrenheit":
                return (value - 273.15) * 9/5 + 32
            else:
                return value
    else:
        return value * unit_maps[category][from_unit] / unit_maps[category][to_unit]

# UI
st.subheader("Select Conversion Type")
conversion_type = st.selectbox("Conversion Type", conversion_types)

if conversion_type == "Temperature":
    from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])
else:
    unit_list = list(unit_maps[conversion_type].keys())
    from_unit = st.selectbox("From Unit", unit_list)
    to_unit = st.selectbox("To Unit", unit_list)

value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

if st.button("Convert"):
    result = convert(value, from_unit, to_unit, conversion_type)
    st.success(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")