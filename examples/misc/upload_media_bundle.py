#!/usr/bin/env python
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""This example uploads an HTML5 zip file as a media bundle."""


import argparse
import sys

import requests

from google.ads.google_ads.client import GoogleAdsClient
from google.ads.google_ads.errors import GoogleAdsException


BUNDLE_URL = 'https://goo.gl/9Y7qI2'

def main(client, customer_id):
    media_file_operation = client.get_type('MediaFileOperation', version='v4')
    media_file = media_file_operation.create
    media_file.name.value = 'Ad Media Bundle'
    media_file.type = (client.get_type('MediaTypeEnum',
                                       version='v4').MEDIA_BUNDLE)
    # Download the ZIP as bytes from the URL
    media_file.media_bundle.data.value = requests.get(BUNDLE_URL).content

    media_file_service = client.get_service('MediaFileService', version='v4')

    try:
        mutate_media_files_response = (
            media_file_service.mutate_media_files(customer_id,
                                                  [media_file_operation])
        )
        print(f'Uploaded file with resource name '
              f'"{mutate_media_files_response.results[0].resource_name}"')

    except GoogleAdsException as ex:
        print(f'Request with ID "{ex.request_id}" failed with status '
              f'"{ex.error.code().name}" and includes the following errors: ')
        for error in ex.failure.errors:
            print(f'\tError with message "{error.message}".')
            if error.location:
                for field_path_element in error.location.field_path_elements:
                    print(f'\t\tOn field: {field_path_element.field_name}')
        sys.exit(1)


if __name__ == '__main__':
    # GoogleAdsClient will read the google-ads.yaml configuration file in the
    # home directory if none is specified.
    google_ads_client = GoogleAdsClient.load_from_storage()

    parser = argparse.ArgumentParser(
        description='Uploads a media bundle.')
    # The following argument(s) should be provided to run the example.
    parser.add_argument('-c', '--customer_id', type=str,
                        required=True, help='The Google Ads customer ID.')
    args = parser.parse_args()

    main(google_ads_client, args.customer_id)
