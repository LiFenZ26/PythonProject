from pages.download_page import DownloadPage


def test_download(page):
    url = "http://the-internet.herokuapp.com/download"

    download_page = DownloadPage(page)
    download_page.open(url)
    file_name = download_page.get_third_file_name()
    download_name = download_page.download_third_file()
    assert file_name == download_name