# Azure Cloud Devops Automation

## Overview

This project demonstrates an automated cloud deployment workflow on Microsoft Azure using **Terraform** for Infrastructure as Code and **GitHub Actions** for CI/CD automation.

The pipeline is responsible for:

- Provisioning Azure infrastructure using Terraform  
- Building and pushing a Docker container image  
- Deploying the containerized application to Azure  
- Ensuring consistent and repeatable deployments  

The architecture follows **immutable infrastructure principles**, meaning infrastructure components are replaced rather than modified during updates. This approach improves reliability, reduces configuration drift, and makes rollbacks safer and more predictable.

---

## Tech Stack

- Microsoft Azure  
- Terraform  
- GitHub Actions  
- Docker  

---

## Key Features

- Fully automated infrastructure provisioning  
- Containerized application deployment  
- CI/CD pipeline triggered on code push  
- Reproducible and stateless deployments  
- Infrastructure managed as code  

---

## Deployment Flow

1. Code is pushed to the `main` branch  
2. GitHub Actions workflow is triggered  
3. Docker image is built and pushed to Docker Hub  
4. Terraform provisions or updates Azure resources  
5. Application is deployed using immutable deployment practices  

---

## Architecture Diagram


Developer
   │
   ▼
GitHub Repository (main branch)
   │
   ▼
GitHub Actions CI/CD Pipeline
   │
   ├── Build Docker Image
   ├── Push Image to DockerHub
   └── Terraform Apply
            │
            ▼
      Azure Infrastructure
      ├── Resource Group
      ├── Virtual Network
      ├── Subnet
      ├── Network Security Group
      ├── Public IP
      └── Linux Virtual Machine
                │
                ▼
        Cloud-init (Auto Setup)
                │
                ▼
         Docker Container Running App
                │
                ▼
           Publicly Accessible Application

---

## Objective

The goal of this project is to demonstrate practical DevOps skills by combining cloud infrastructure automation, containerization, and CI/CD into a single streamlined pipeline.
