!apt-get dist-upgrade
!apt-get install -y software-properties-common
!apt-get install -y build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev autotools-dev autoconf automake libtool
!apt-get install sqlite3
!git clone https://github.com/OSGeo/PROJ.git
!cd PROJ && ./autogen.sh && ./configure && make && make install && cd ..
!git clone https://github.com/OSGeo/gdal.git
!cd gdal/gdal && ./autogen.sh && ./configure --with-proj=/usr/local && make && make install && cd ../..
#!apt-get install -y gdal-bin
#!apt-get install -y libgdal-dev
#!gdal-config --version
!apt-get install libspatialindex-dev python3.7 python3.7-dev virtualenv
!export CPLUS_INCLUDE_PATH=/usr/include/gdal
!export C_INCLUDE_PATH=/usr/include/gdal
!virtualenv -p /usr/bin/python3.7 myenv
!source myenv/bin/activate; git clone https://github.com/Toblerity/Shapely.git; cd Shapely; python3 setup.py install; cd ..; rm -rf Shapely; pip install solaris; pip install geopandas
!rm -rf PROJ gdal
