> Script para transformar la base de datos de excel de correos de México en archivos JSON y CSV.

En este repositorio creamos un script que permite transformar el excel que provee correos de mexico en formatos más amigables para la ingesta de datos.

El archivo que se usa como origen se puede obtener en su sitio oficial:

[https://www.correosdemexico.gob.mx/SSLServicios/ConsultaCP/CodigoPostal_Exportar.aspx](https://www.correosdemexico.gob.mx/SSLServicios/ConsultaCP/CodigoPostal_Exportar.aspx)


Para una mejor experiencia, se sugiere instalar Anaconda (https://www.anaconda.com/) y crear un entorno virtual.

**Anaconda**

```plaintext
conda create -n mpostalcode python=3.10
conda activate mpostalcode
```

Los requerimentos se encuentran en el archivo _requirements.txt_ el cual se puede ejecutar de la siguiente manera

```plaintext
pip -r requirements.txt
```
