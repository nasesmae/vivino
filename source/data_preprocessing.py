import pandas as pd
import pycountry

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('data/csv_files/countries.csv')

# Function to convert country code to country name
def get_country_name(code):
    try:
        country = pycountry.countries.get(alpha_2=code)
        if country:
            return country.name
        else:
            return None
    except LookupError:
        return None

# Translate country codes to country names
df['name'] = df['code'].apply(get_country_name)

# Write the modified DataFrame back to the CSV file, overwriting the existing file
df.to_csv('data/csv_files/countries.csv', index=False)

print("Translation complete. 'name' column updated.")

import time
import pandas as pd
import re
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderUnavailable

# Function to extract region name enclosed within single quotes
def extract_region_name(name):
    match = re.search(r"'(.*?)'", name)
    if match:
        return match.group(1)
    else:
        return None

# Function to translate region names with retry logic
def translate_region_info(region_name, country_code):
    geolocator = Nominatim(user_agent="wine_region_translator")
    attempts = 3
    for attempt in range(attempts):
        try:
            location = geolocator.geocode(region_name + ', ' + country_code)
            if location:
                # Use reverse geocoding to retrieve address information
                reverse_location = geolocator.reverse((location.latitude, location.longitude))
                if reverse_location:
                    postal_code = reverse_location.raw.get('address', {}).get('postcode')
                    latitude = location.latitude
                    longitude = location.longitude
                    return postal_code, latitude, longitude
                else:
                    postal_code = None
                    latitude = location.latitude
                    longitude = location.longitude
                    return postal_code, latitude, longitude
            else:
                postal_code = None
                latitude = None
                longitude = None
                return postal_code, latitude, longitude
        except GeocoderUnavailable as e:
            print(f"Geocoding service unavailable. Retrying ({attempt + 1}/{attempts})...")
            time.sleep(1)  # Wait for 1 second before retrying
    print(f"Failed to translate region name: {region_name}")
    postal_code = None
    latitude = None
    longitude = None
    return postal_code, latitude, longitude

# Read the regions CSV file into a pandas DataFrame
regions_df = pd.read_csv('data/csv_files/regions.csv')

# Function to process and update DataFrame
def process_dataframe(df):
    # Extract region name enclosed within single quotes and add it to a new column
    df['extracted_name'] = df['name'].apply(extract_region_name)

    # Use extracted name if available, else use original name
    df['final_name'] = df.apply(lambda row: row['extracted_name'] if row['extracted_name'] else row['name'], axis=1)

    # Translate region names with retry logic using extracted name if available, else use original name
    translated_info = df.apply(lambda row: translate_region_info(row['final_name'], row['country_code']), axis=1)
    postal_code, latitude, longitude = zip(*translated_info)
    df['postal_code'] = postal_code
    df['latitude'] = latitude
    df['longitude'] = longitude

    # Drop the extracted_name column
    df.drop(columns=['extracted_name'], inplace=True)

    return df

# Process and update DataFrame
regions_df = process_dataframe(regions_df)

# Reorder columns to match the desired format
regions_df = regions_df[['id', 'final_name', 'country_code', 'postal_code', 'latitude', 'longitude']]

# Write the modified DataFrame to the CSV file
regions_df.to_csv('data/csv_files/regions_processed.csv', index=False)

print("Processing complete. New CSV file created.")

