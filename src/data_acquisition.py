from request_handlers import generalRequestHandler
from authentication import generate_token
from sag_utils import common
from preprocess_data import preprocess



def main():
    # Credentials to authenticate with the API
    module_api_name = "Leads"
    client_id = "1000.6H0OTK7ATTPUHYZ6AM0240RNG7LK3F"
    client_secret = "08c4149dbbff5618061ccc7d08e573d6921d0550a7"
    redirect_uri = "https://www.google.com/"
    code = "1000.d37ccc2b5b516955724e8e3f4788030d.be7e604705bc75c11904f0544e86f7d5"

    # Set up a logger to log progress
    logger = common.get_logger('get_' + module_api_name)
    logger.info(f'code project being used is: {code}')

    # Generate an access token using the provided credentials
    access_token = generate_token.generate_access_token(client_id, client_secret, redirect_uri, code)

    # Use the access token to generate a refresh token
    refresh_token = generate_token.refresh_access_token(access_token['refresh_token'], client_id, client_secret)

    # Fetch data from the API using the refresh token
    json_data = generalRequestHandler.get_all_leads(refresh_token)


    # Convert the fetched data from JSON to a pandas DataFrame
    Dataframe = preprocess.json_to_dataframe(json_data)

    # Save the DataFrame to a CSV file in the "files_data" directory
    preprocess.save_dataframe_to_csv(Dataframe)


    logger.info('The CSV file has been generated successfully.')
if __name__ == "__main__":
    main()

