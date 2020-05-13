Instalar MongoDB mediante Vagrant
================

Uso de Vagrant para ejecutar la última versión de MongoDB desde su repositorio oficial (se incluyen datos de muestra para pruebas).

La versión original de esta idea está https://github.com/bobthecow/vagrant-mongobox.

1. Instale VirtualBox.

2. En su terminal, ejecute lo siguiente:

   ```
   gem install vagrant
   git clone --recursive https://github.com/mcardenas/vagrant-mongodb-box.git MongoDB
   cd MongoDB
   vagrant up
   ```

   Espere unos instantes.
   
3. Ahora tiene una instancia de un servicio MongoDB levantaba en la URL localhost:27018.

   ```
   mongo --port 17017
   ```