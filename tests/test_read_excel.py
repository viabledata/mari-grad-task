import os
import pytest

from pathlib import Path
TEST_DATA_PATH = Path(__file__).parent / "test_files"


@pytest.mark.usefixtures("test_client")
class TestReadFile:
    url = "/v1/read"

    def test_read_file(self):
        data = {
            "file_path": os.path.join(TEST_DATA_PATH, "test_register_data.xlsx")
        }
        # print(f"here....path: {TEST_DATA_PATH}")
        result = self.client.post(self.url, json=data, content_type="application/json")
        # return result
