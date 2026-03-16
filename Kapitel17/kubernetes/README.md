# Kubernetes mit minikube

Dieses Verzeichnis enthält Beispiel-Konfigurationen für Kubernetes (K8s), wie sie in Kapitel 17 beschrieben werden. Die Beispiele zeigen, wie man mit `kubectl` und `minikube` einfache Deployments und Services erstellt.

## Voraussetzungen

- Installation von [kubectl](https://kubernetes.io/de/docs/tasks/tools/install-kubectl/)
- Installation von [minikube](https://kubernetes.io/de/docs/tasks/tools/install-minikube/)

## Minikube starten

```bash
minikube start
```

## Nginx-Beispiel: Deployment

Das [Deployment](nginx-deployment.yaml) definiert eine Nginx-Webanwendung mit 3 Repliken.

**Befehl zum Anwenden:**

```bash
kubectl apply -f nginx-deployment.yaml
```

## Nginx-Beispiel: Service

Der [Service](nginx-service.yaml) macht die Webanwendung innerhalb des Clusters erreichbar.

**Befehl zum Anwenden:**

```bash
kubectl apply -f nginx-service.yaml
```

## Port Forwarding

Um die Anwendung lokal zu testen, können Sie Port Forwarding verwenden:

```bash
kubectl port-forward service/webapp-service 8899:80
```

Anschließend ist die Anwendung unter [http://localhost:8899](http://localhost:8899) erreichbar.