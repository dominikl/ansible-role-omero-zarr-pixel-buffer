OMERO Zarr Pixel Buffer
======================

Install OMERO Zarr Pixel Buffer into existing OMERO.server

Requirements
------------

OMERO.server installation

Role Variables
--------------

The following variables can be set for this role (see `defaults/main.yml` for defaults):

- **omero_zarr_pixel_buffer_user**: User account under which OMERO.server runs and the pixel buffer JARs will be installed.
- **omero_zarr_pixel_buffer_folder**: Target directory where the pixel buffer JARs will be installed (typically the OMERO.server `lib/server` directory).
- **zarrpixelbuffer_jar**: Primary OMERO Zarr Pixel Buffer JAR definition.
  - `name`: Artifact ID of the JAR (e.g. `omero-zarr-pixel-buffer`).
  - `group`: Maven group path of the artifact (e.g. `com/glencoesoftware/omero`).
  - `version`: Version of the artifact to install.
- **zarrpixelbuffer_dep_jars**: List of dependency JARs required by the pixel buffer.
  - `name`: Artifact ID of the dependency.
  - `group`: Maven group path of the dependency.
  - `version`: Version of the dependency.
- **glencoe_artifactory_baseurl**: Base URL for the Glencoe Software Artifactory repository used to download the main pixel buffer JAR.
- **maven_artifactory_url**: Maven Central (or other Maven) repository URL used to download dependency JARs.


Example Playbook
----------------

```
- hosts: localhost
  roles:
    - role: ome.omero_zarr_pixel_buffer
```

Author Information
------------------

ome-devel@lists.openmicroscopy.org.uk
