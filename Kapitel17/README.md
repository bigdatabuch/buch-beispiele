# Kapitel 17: Test und Betrieb von Big-Data-Systemen

Dieses Kapitel behandelt DevOps-Praktiken, Teststrategien und Betriebsmodelle für Big-Data-Systeme.

## Übersicht der Code-Beispiele

### Kubernetes-Beispiele

Das Verzeichnis `kubernetes/` enthält Beispiele für die Orchestrierung von Containern mit Kubernetes:

- **[kubernetes/README.md](kubernetes/README.md)** — Anleitung zur Einrichtung und Verwendung von Kubernetes mit minikube
- **[nginx-deployment.yaml](kubernetes/nginx-deployment.yaml)** — Kubernetes Deployment-Manifest für eine Nginx-Webanwendung mit 3 Repliken
- **[nginx-service.yaml](kubernetes/nginx-service.yaml)** — Kubernetes Service-Manifest für den Zugriff auf die Webanwendung innerhalb des Clusters

Diese Beispiele veranschaulichen die grundlegenden Konzepte von Deployments und Services in Kubernetes.

## Verwandte Kapitel

- **Kapitel 11** — Kafka und Stream Processing (Docker Compose Beispiele)
- **Kapitel 13** — Spark, Flink und Hadoop (Container- und Cluster-Konfigurationen)
- **Kapitel 14** — Data Lakehouse mit Delta Lake (Docker Compose, S3)

---

*Letzte Aktualisierung: 14. März 2026*