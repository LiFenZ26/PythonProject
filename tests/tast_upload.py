from pages.upload_page import UploadPage


def test_upload(page):
    url = "http://the-internet.herokuapp.com/upload"

    upload_page = UploadPage(page)
    upload_page.open(url)
    upload_page.upload_file("test_data/test_image.png")

    assert upload_page.get_success_message() == "File Uploaded!"
    assert upload_page.get_uploaded_file_name() == "test_image.png"
