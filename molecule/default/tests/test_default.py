import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_httpd_installed(host):
    apache = host.package("httpd")

    assert apache.is_installed


def test_httpd_listener(host):
    listener = host.socket("tcp://0.0.0.0:80")

    assert listener.is_listening


def test_httpd_service(host):
    service = host.service("httpd")

    assert service.is_enabled
    assert service.is_running


def test_httpd_path(host):
    path = host.file("/etc/httpd")

    assert path.is_directory
