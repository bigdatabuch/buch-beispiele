# spark/Dockerfile
FROM bitnami/spark:latest

# Bitnami-Images laufen als non-root (1001). Zum Installieren kurz root werden:
USER root
# 'install_packages' ist in Bitnami-Images vorhanden (wrappt apt-get)
RUN install_packages python3 && ln -sf /usr/bin/python3 /usr/bin/python

# PySpark explizit auf python3 setzen
ENV PYSPARK_PYTHON=python3 \
    PYSPARK_DRIVER_PYTHON=python3

# Zurück zum Standard-User
USER 1001
