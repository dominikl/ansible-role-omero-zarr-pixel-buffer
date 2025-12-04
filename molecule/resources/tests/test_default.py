import os
import re

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


OMERO = '/opt/omero/web/OMERO.web/bin/omero'
# Need to match 5.6.dev2
# VERSION_PATTERN = re.compile('(\d+)\.(\d+)\.(\d+)-ice36-')
VERSION_PATTERN = re.compile(r'(\d+)\.(\d+)\.(\w+)')


# check if omero web is sunning
def test_nginx_gateway(host):
    out = host.check_output('curl -L localhost')
    assert 'OMERO.web - Login' in out

# check if the omero server is sunning
def test_service_running_and_enabled(host):
    assert host.service('omero-server').is_running
    assert host.service('omero-server').is_enabled

def omero_zarr_pixel_buffer(host):
    # TODO: Implement!
    pass

def test_nginx_gateway(host):
    out = host.check_output('curl -L localhost')
    assert 'OMERO.web - Login' in out
