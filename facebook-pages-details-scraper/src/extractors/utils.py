thondef clean_data(data):
    # Helper function to clean the scraped data
cleaned_data = {key: value.strip() if isinstance(value, str) else value for key, value in data.items()}
return cleaned_data