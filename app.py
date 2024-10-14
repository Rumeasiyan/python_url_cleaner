import pandas as pd
import re

# Read the CSV file containing the original URLs
df = pd.read_csv('urls.csv')

# Define a function to clean and reformat the URLs


def clean_url_ae(url):
    # Remove everything after '?' but keep the menu parameter
    base_url = url.split('?')[0]  # Get the base URL before '?'

    # Use regex to match the new format with 'menu=' parameter
    match = re.search(r'menu=([^&]*)', url)
    if match:
        # Get the menu parameter value
        menu_param = match.group(0)
        # Reconstruct the cleaned URL
        cleaned_url = f"{base_url}?{menu_param}"
    else:
        cleaned_url = base_url  # If there is no menu parameter, return the base URL

    return cleaned_url


def clean_url_athelia(url):
    # Use regex to extract the pid value
    match = re.search(r'pid=(\d+)', url)
    if match:
        pid = match.group(1)
        # Format the cleaned URL
        cleaned_url = f"https://athleta.gap.com/browse/product.do?pid={pid}"
        return cleaned_url
    else:
        return url  # Return original if no pid found

def clean_url_gap(url):
    # Use regex to extract the pid value
    match = re.search(r'pid=(\d+)', url)
    if match:
        pid = match.group(1)
        # Format the cleaned URL
        cleaned_url = f'https://www.gap.com/browse/product.do?pid={pid}'
        return cleaned_url
    else:
        return url  # Return original if no pid found
    
def clean_url_soma(url):
    # Use regex to remove everything after the '?' character
    cleaned_url = re.sub(r'\?.*$', '', url)
    return cleaned_url

def clean_url_vs(url):
    # Use regex to remove everything after the '?' character
    cleaned_url = re.sub(r'\?.*$', '', url)
    return cleaned_url


def clean_url_nike(url):
    # Split the URL by '/'
    parts = url.split('/')

    # Check if there are enough parts to remove the 6th element (index 5)
    if len(parts) > 5:
        # Remove the 6th element
        parts.pop(5)

    # Join the remaining parts back into a cleaned URL
    cleaned_url = '/'.join(parts)

    return cleaned_url


def clean_url_adoreme(url):
    # Split the URL by '/'
    parts = url.split('/')

    # Check if there are enough parts to remove the 5th element (index 4)
    if len(parts) > 4:
        # Remove the 5th element
        print('Removing:', parts[4])
        parts.pop(4)

    # Join the remaining parts back into a cleaned URL
    cleaned_url = '/'.join(parts)

    return cleaned_url


def clean_url_gym_shark(url):
    # Split the URL by '/'
    parts = url.split('/')

    # Check if there are enough parts to remove the 6th element (index 5)
    if len(parts) > 5:
        # Remove the 6th element
        print('Removing:', parts[5])
        parts.pop(5)

    # Join the remaining parts back into a cleaned URL
    cleaned_url = '/'.join(parts)

    return cleaned_url


def clean_url_lulu(url):
    # Use regex to remove everything after the '?' character
    cleaned_url = re.sub(r'\?.*$', '', url)
    return cleaned_url


def clean_url_skims(url):
    # Split the URL by '/'
    parts = url.split('/')

    # Check if there are enough parts to remove the 6th element (index 5)
    if len(parts) > 5:
        # Remove the 6th element
        print('Removing:', parts[5])
        parts.pop(5)

    # Join the remaining parts back into a cleaned URL
    cleaned_url = '/'.join(parts)

    return cleaned_url


# Apply the cleaning function to the 'url' column
df['cleaned_url'] = df['url'].apply(clean_url_skims)

# Save the new DataFrame to a new CSV file
df.to_csv('cleaned_urls.csv', index=False)

print("URLs have been cleaned and saved to 'cleaned_urls.csv'.")
