import requests
import csv

# Function to make an HTTP GET request and save the result to a CSV file
def make_get_request_and_save_to_csv(url, csv_filename):
    try:
        # Disable SSL verification
        response = requests.get(url, verify=False)

        # Extract the HTTP status code
        http_status_code = response.status_code

        # Write the URL and HTTP status code to a CSV file
        with open(csv_filename, 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([f"{url} checked", http_status_code])
        
        print(f"HTTP request to {url} successful. HTTP return code: {http_status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Function to read URLs from a text file and process them
def process_urls_from_txt(input_txt_filename, output_csv_filename):
    with open(input_txt_filename, 'r') as txt_file:
        for line in txt_file:
            url = line.strip()  # Remove leading/trailing whitespace and newline characters
            if url:
                make_get_request_and_save_to_csv(url, output_csv_filename)

# Example usage:
if __name__ == "__main__":
    input_txt_filename = "URLS.txt"  # Replace with your input text file name
    output_csv_filename = "results.csv"  # Replace with the desired output CSV filename

    # Create or truncate the output CSV file
    with open(output_csv_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["URL", "HTTP Return Code"])  # Write the header row

    process_urls_from_txt(input_txt_filename, output_csv_filename)

#ey
#confidential
#secret
#ernst & young
#classified
#passwords
#secret