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
- Ansible 

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

## System Architecture

```
                    ┌────────────────────────────┐
                    │        Developer           │
                    │       Code Commit          │
                    └─────────────┬──────────────┘
                                  │
                                  ▼
                    ┌────────────────────────────┐
                    │      GitHub Repository     │
                    │        (main branch)       │
                    └─────────────┬──────────────┘
                                  │  Webhook Trigger
                                  ▼
┌────────────────────────────────────────────────────────────────┐
│                    GitHub Actions Pipeline                     │
│----------------------------------------------------------------│
│  1. Checkout Source Code                                       │
│  2. Build Docker Image                                         │
│  3. Push Image to DockerHub                                    │
│  4. Authenticate with Azure ( Service Principal)         │
│  5. Terraform Init → Plan → Apply                              │
└─────────────┬──────────────────────────────────────────────────┘
              │
              ▼
┌────────────────────────────────────────────────────────────────┐
│                         Microsoft Azure                        │
│----------------------------------------------------------------│
│  Resource Group                                                │
│    ├── Virtual Network                                         │
│    ├── Subnet                                                  │
│    ├── Network Security Group                                  │
│    ├── Public IP                                               │
│    └── Linux Virtual Machine                                   │
└─────────────┬──────────────────────────────────────────────────┘
              │  cloud-init provisioning
              ▼
┌────────────────────────────────────────────────────────────────┐
│                     Virtual Machine Runtime                    │
│----------------------------------------------------------------│
│  • Install Docker Engine                                       │
│  • Pull latest container image                                 │
│  • Run container (port mapping 80:5000)                        │
└─────────────┬──────────────────────────────────────────────────┘
              │
              ▼
┌────────────────────────────────────────────────────────────────┐
│                 Publicly Accessible Application                │
│                 http://<vm-public-ip>                          │
└────────────────────────────────────────────────────────────────┘
```

## Objective

The goal of this project is to demonstrate practical DevOps skills by combining cloud infrastructure automation, containerization, and CI/CD into a single streamlined pipeline.

---

## Engineering Highlights

- Built and managed cloud infrastructure entirely through Terraform configuration files  
- Developed an automated CI/CD pipeline using GitHub Actions to streamline deployments  
- Followed immutable infrastructure practices to prevent configuration drift  
- Configured automated VM initialization with cloud-init scripts  
- Integrated Docker image build and deployment into the infrastructure workflow  
- Enabled complete environment lifecycle management using `terraform apply` and `terraform destroy`  
- Protected sensitive configuration data using encrypted GitHub repository secrets  
- Created a seamless automation flow from source code push to live deployment  

---

## DevOps Principles Applied

- Infrastructure as Code (IaC)  
- Continuous Integration and Continuous Deployment  
- Azure Cloud Networking and Resource Architecture  
- Immutable Deployment Strategy  
- Container-Based Application Delivery  
- Automated Infrastructure Provisioning  
- Cloud Resource Lifecycle and State Management  

---
