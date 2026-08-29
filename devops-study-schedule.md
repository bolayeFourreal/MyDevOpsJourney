# 16-Week DevOps Mastery Study Schedule (2026 Edition)

This study schedule is a highly structured, 16-week curriculum designed to guide you from foundational software operations to advanced cloud infrastructure engineering. It maps the 12 core phases and the DevSecOps bonus module from the official 2026 DevOps Roadmap into a realistic, weekly execution plan.

Each week features clear objectives, hands-on milestones, and direct references to mostly free curated resources from your study guide.

---

## 📅 Roadmap at a Glance

| Week | Stage & Topic | Estimated Hours | Key Project/Deliverable | Primary Resource(s) |
|---|---|---|---|---|
| **Week 1** | Stage 1: Git & Version Control | 6–8 hrs | Personal Portfolio Git Repository | Atlassian Git, Learn Git Branching |
| **Week 2** | Stage 2: Programming Fundamentals | 8–10 hrs | CLI Utility (e.g., Log Parser) | Python Crash Course / Go by Example |
| **Week 3** | Stage 2: Scripting & Automation | 8–10 hrs | Systems Automation Script | Automate the Boring Stuff |
| **Week 4** | Stage 3: Linux Systems & OS Foundations | 8–10 hrs | Ubuntu OS VM Lab Setup | Tutorialspoint OS, FreeCodeCamp Handbook |
| **Week 5** | Stage 3: Advanced Shell Scripting | 8–10 hrs | Backup & Rotation Script in Bash | Linux Commands Handbook, ShellScript.sh |
| **Week 6** | Stage 4: Networking & Security Protocols | 6–8 hrs | Local DNS Lookup & Wireshark Lab | Cloudflare OSI Guide, How DNS Works |
| **Week 7** | Stage 5: Server Management & Proxies | 8–10 hrs | Nginx Reverse Proxy with SSL | The NGINX Handbook, Cloudflare Proxies |
| **Week 8** | Stage 6: Containers & Docker Foundations | 8–10 hrs | Dockerized Web Application | Docker Crash Course (Nana), OCI Spec |
| **Week 9** | Stage 6: Multi-Container Docker Compose | 8–10 hrs | Three-Tier App via Docker Compose | TechWorld with Nana (Compose Tutorial) |
| **Week 10** | Stage 7: Kubernetes Core Architecture | 10–12 hrs | Single-node K8s Cluster Deployment | Kubernetes Learning Path (Microsoft) |
| **Week 11** | Stage 7: Advanced K8s Administration | 10–12 hrs | Helm Chart Packaging & TLS Automation | KodeKloud K8s, cert-manager |
| **Week 12** | Stage 8: Infrastructure as Code (Terraform) | 10–12 hrs | AWS/Azure Resource Provisioning | HashiCorp Terraform Tutorials |
| **Week 13** | Stage 9: CI/CD Pipeline Design | 10–12 hrs | Automated GitHub Actions CI/CD | GitHub Actions Workflow Syntax |
| **Week 14** | Stage 10: Observability & Log Management | 10–12 hrs | Prometheus & Grafana Monitoring | Grafana & Prometheus Tutorial |
| **Week 15** | Stage 11: Cloud Architecture & Scaling | 8–10 hrs | Cloud Security & Admin Lab | AWS Well-Architected / AZ-900 |
| **Week 16** | Stage 12 & Bonus: SDLC & DevSecOps | 8–10 hrs | Trivy Container Security Scan | OWASP DevSecOps, SLSA, Trivy |

---

## 📚 Canonical Literature Integration

To build a deep understanding of DevOps culture, operations theory, and team structures, align your weekly learning with these canonical texts:
* **Weeks 1–3 (Mindset & Culture)**: Read *The Phoenix Project* by Gene Kim, Kevin Behr, and George Spafford.
* **Weeks 4–6 (Agility & Scaling)**: Read *The DevOps Handbook* by Gene Kim, Patrick Debois, John Willis, and Jez Humble.
* **Weeks 7–9 (Team Organization)**: Read *Team Topologies* by Matthew Skelton and Manuel Pais, alongside *Effective DevOps* by Jennifer Davis and Ryn Daniels.
* **Weeks 10–12 (Software Performance Science)**: Read *Accelerate* by Nicole Forsgren, Jez Humble, and Gene Kim.
* **Weeks 13–14 (Delivery & Production)**: Read *Continuous Delivery* by Jez Humble and David Farley, or *Fundamentals of DevOps and Software Delivery* by Yevgeniy Brikman.
* **Weeks 15–16 (Operations & Scale)**: Read *Site Reliability Engineering* by Betsy Beyer, Chris Jones, Jennifer Petoff, and Niall Richard Murphy (Google SRE Book).

---

## 🛠️ Detailed Weekly Curriculum

### Week 1: Git & Version Control (Stage 1)
*   **Focus**: Mastery of source code tracking and collaboration.
*   **Concepts**: Centralized vs. Distributed VCS, git lifecycle (working directory, staging area, local/remote repository), branch models (GitFlow, trunk-based).
*   **Commands to Master**: `git init`, `git clone`, `git status`, `git add`, `git commit`, `git branch`, `git merge`, `git checkout -b`, `git pull`, `git push`, `git fetch`, `git rebase`.
*   **Practical Project**: Create a GitHub repository to track this 16-week study path. Commit daily, practice merging branches locally, and resolve a manual merge conflict.
*   **Resources**:
    *   [Pro Git Book](https://git-scm.com/book/en/v2) (Chapters 1-3)
    *   [Learn Git Branching](https://learngitbranching.js.org/) (Interactive game)
    *   [Learn Git by Atlassian](https://www.atlassian.com/git)

### Week 2: Programming Fundamentals (Stage 2)
*   **Focus**: Learning the syntax of Python, Go, or JavaScript. Python is recommended for its high readability and broad system utility.
*   **Concepts**: Variables, data types, conditions (`if/else`), loops (`for`, `while`), lists/arrays, dictionaries/maps, basic functions, error/exception handling.
*   **Practical Project**: Write a console-based calculator or a text-based inventory management script in your chosen language.
*   **Resources**:
    *   Python: [Python Crash Course](https://ehmatthes.github.io/pcc/)
    *   Go: [Go by Example](https://gobyexample.com/)
    *   JavaScript: [JavaScript Crash Course For Beginners](https://www.youtube.com/watch?v=hdI2bqOjy3c)

### Week 3: Scripting & Automation (Stage 2)
*   **Focus**: Moving from standard syntax to building automation scripts for administrative tasks.
*   **Concepts**: File I/O, parsing JSON/YAML, using standard library modules for interacting with OS directories and environments.
*   **Practical Project**: Write a script that parses an application log file (`access.log`), counts error codes (400, 500), and outputs a summary report in JSON format.
*   **Resources**:
    *   Python: [Automate the Boring Stuff with Python Book](https://automatetheboringstuff.com/)
    *   Go: [Learn Go with Tests](https://quii.gitbook.io/learn-go-with-tests)
    *   JavaScript: [Eloquent JavaScript](https://eloquentjavascript.net/)

### Week 4: Linux Systems & OS Foundations (Stage 3)
*   **Focus**: Operating system layers, core navigation, and distributions (Ubuntu recommended).
*   **Concepts**: Linux kernel vs. user space, boot process, filesystem hierarchy (FHS), file permissions, users and groups.
*   **CLI Commands**: `ls`, `cd`, `mkdir`, `rm`, `cp`, `mv`, `touch`, `cat`, `chmod`, `chown`, `sudo`, `man`.
*   **Practical Project**: Install Ubuntu in a local virtual machine (VirtualBox/VMware) or set up WSL (Windows Subsystem for Linux). Log in, configure a non-root administrative user, and organize directories.
*   **Resources**:
    *   [Operating System - Overview](https://www.tutorialspoint.com/operating_system/os_overview.htm)
    *   [Ultimate Guide: Getting Started With Ubuntu](https://itsfoss.com/getting-started-with-ubuntu/)
    *   [Linux Command Handbook](https://www.freecodecamp.org/news/the-linux-commands-handbook/)

### Week 5: Advanced Shell Scripting (Stage 3)
*   **Focus**: CLI administration and environment automation.
*   **Concepts**: Process management, environment variables, text streams, shell scripting logic (conditional testing, positional parameters).
*   **CLI Commands**: `grep`, `find`, `printenv`, `ps`, `kill`, `top`, `df`, `du`, `tar`, `gzip`, `ssh`, `scp`, `wget`, `curl`.
*   **Practical Project**: Build a robust Bash backup script that compresses a target folder into a `.tar.gz` archive, appends a timestamp to the name, saves it to a backups folder, and prints disk space updates using `df`.
*   **Resources**:
    *   [Shell Scripting Tutorial](https://www.shellscript.sh/)
    *   [Bash Reference Manual](https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html)

### Week 6: Networking & Security Protocols (Stage 4)
*   **Focus**: Inter-system communication layers.
*   **Concepts**: The OSI Model, TCP vs. UDP, IPv4/IPv6 subnetting, ports, firewalls, and security handshakes.
*   **Protocols**: DNS/DNSSEC, HTTPS, SSH, TLS/SSL.
*   **Practical Project**: Set up DNS lookups via CLI, configure simple port forwarding, and trace local connection paths using routing/network commands.
*   **Resources**:
    *   [OSI Model Explained](https://www.cloudflare.com/en-gb/learning/ddos/glossary/open-systems-interconnection-model-osi/)
    *   [How DNS Works](https://howdns.works/) & [How HTTPS Works](https://howhttps.works/)
    *   [Professor Messer's Network+ Course](https://www.professormesser.com/network-plus/n10-008/n10-008-video/n10-008-training-course/)

### Week 7: Server Management & Proxies (Stage 5)
*   **Focus**: Server reliability, traffic routing, caching, and proxy boundaries.
*   **Concepts**: Forward proxies vs. Reverse proxies, load balancing algorithms, HTTP headers, TLS termination, CDN edge logic.
*   **Tools**: Nginx, Apache.
*   **Practical Project**: Set up a local Nginx server acting as a reverse proxy for your Python/Go script from Week 3, complete with basic routing and local SSL/TLS configurations.
*   **Resources**:
    *   [The NGINX Handbook](https://www.freecodecamp.org/news/the-nginx-handbook/)
    *   [What is a reverse proxy?](https://www.cloudflare.com/en-gb/learning/cdn/glossary/reverse-proxy/)
    *   [What is load balancing?](https://www.cloudflare.com/en-gb/learning/performance/what-is-load-balancing/)

### Week 8: Containers & Docker Foundations (Stage 6)
*   **Focus**: Packaging code and system dependencies into consistent runtimes.
*   **Concepts**: Containers vs. VMs, namespaces and cgroups, OCI image specification, layer caching.
*   **CLI Commands**: `docker build`, `docker run`, `docker stop`, `docker ps`, `docker images`, `docker volume`, `docker network`.
*   **Practical Project**: Write a multi-stage Dockerfile to containerize your python/Go program, optimizing the build to minimize image size.
*   **Resources**:
    *   [Learning Containers From The Bottom Up](https://iximiuz.com/en/posts/container-learning-path/)
    *   [Docker Tutorial for Beginners by TechWorld with Nana](https://www.youtube.com/watch?v=3c-iBn73dDE)
    *   [OCI Specification](https://github.com/opencontainers/image-spec/blob/main/spec.md)

### Week 9: Multi-Container Docker Compose (Stage 6)
*   **Focus**: Coordinating multi-tier architectures.
*   **Concepts**: Docker Compose YAML schema, service dependency order (`depends_on`), persistent storage volumes, private virtual networks.
*   **Practical Project**: Build a docker-compose deployment featuring a frontend web container (Nginx), an API/backend container (Python/Go), and a database container (PostgreSQL/MySQL) sharing data via persistent volumes.
*   **Resources**:
    *   [Ultimate Docker Compose Tutorial by TechWorld with Nana](https://www.youtube.com/watch?v=SXwC9fSwct8)
    *   [What are Containers?](https://cloud.google.com/learn/what-are-containers)

### Week 10: Kubernetes Core Architecture (Stage 7)
*   **Focus**: Container orchestration fundamentals.
*   **Concepts**: Control Plane (API Server, Etcd, Scheduler, Controller Manager) vs. Worker Nodes (Kubelet, Kube-proxy, Container Runtime). K8s resources: Pods, ReplicaSets, Deployments, Services, ConfigMaps, Secrets, Ingress.
*   **Practical Project**: Deploy a local single-node cluster using Minikube or Kind. Write YAML manifests to deploy your containerized app with 3 replicas and expose it with a K8s Service.
*   **Resources**:
    *   [Kubernetes Crash Course for Absolute Beginners](https://www.youtube.com/watch?v=s_o8dwzRlu4)
    *   [Kubernetes Learning Path - Microsoft](https://azure.microsoft.com/en-us/resources/kubernetes-learning-path/)
    *   [Primer: How Kubernetes Came to Be](https://thenewstack.io/primer-how-kubernetes-came-to-be-what-it-is-and-why-you-should-care/)

### Week 11: Advanced Kubernetes Administration (Stage 7)
*   **Focus**: Helm packaging, storage, stateful services, and routing.
*   **Concepts**: StatefulSets, DaemonSets, PersistentVolumes (PV) & PVC, Helm charts, Service Meshes, automated TLS, and external DNS.
*   **Tools**: kubectl, Helm, cert-manager.
*   **Practical Project**: Package your multi-container application into a reusable Helm chart. Configure ingress rules and use `cert-manager` for self-signed or automated TLS certificates.
*   **Resources**:
    *   [Certified Kubernetes Administrator (CKA) with Practice Tests](https://www.udemy.com/course/certified-kubernetes-administrator-with-practice-tests/)
    *   [Learn Kubernetes by KodeKloud](https://kodekloud.com/learning-path-kubernetes/)
    *   [Learn how to automate TLS - cert-manager](https://cert-manager.io/docs/)

### Week 12: Infrastructure as Code (Stage 8)
*   **Focus**: Provisioning and configuration via markup models.
*   **Concepts**: Declarative vs. Imperative IaC, immutable infrastructure, state files, dry runs (`terraform plan`), module structuring.
*   **Tools**: Terraform, Ansible.
*   **Practical Project**: Write Terraform configuration manifests to provision a basic cloud resource group containing a virtual machine and a security network block.
*   **Resources**:
    *   [GUIs, CLI, APIs: Learn Basic Terms of IaC](https://thenewstack.io/guis-cli-apis-learn-basic-terms-of-infrastructure-as-code/)
    *   [Official Terraform Tutorials](https://learn.hashicorp.com/terraform)
    *   [Terraform Course by freeCodeCamp on YouTube](https://www.youtube.com/watch?v=SLB_c_ayRMo)

### Week 13: CI/CD Pipeline Design (Stage 9)
*   **Focus**: Continuous automation pipelines.
*   **Concepts**: Pipeline triggers, runners/agents, execution stages (lint, build, unit test, integration test, publish, deploy), secret management, environment isolation.
*   **Tools**: GitHub Actions, GitLab CI/CD, or Jenkins.
*   **Practical Project**: Design a fully automated GitHub Actions workflow file (`.github/workflows/main.yml`) that lints your code, builds your Docker image, pushes it to Docker Hub on every git commit, and utilizes secure GitHub Secrets.
*   **Resources**:
    *   [CI/CD Pipeline: A Gentle Introduction](https://semaphoreci.com/blog/cicd-pipeline)
    *   [Learn GitHub Actions on Microsoft Learn](https://learn.microsoft.com/en-us/users/githubtraining/collections/n5p4a5z7keznp5)
    *   [GitHub Actions Tutorial by Tech World with Nana](https://www.youtube.com/watch?v=R8_veQiYBjI)

### Week 14: Observability & Log Management (Stage 10)
*   **Focus**: Production monitoring and log aggregation.
*   **Concepts**: Metrics vs. Logs vs. Traces, pull vs. push metrics, alerting thresholds, centralized log dashboards.
*   **Tools**: Prometheus, Grafana, Elastic Stack (Kibana).
*   **Practical Project**: Deploy Prometheus and Grafana on your Kubernetes cluster. Import a pre-configured node-exporter dashboard to visualize node CPU, memory, and network usage.
*   **Resources**:
    *   [What Is Observability? Comprehensive Beginners Guide](https://devopscube.com/what-is-observability/)
    *   [Learn Prometheus Tutorials](https://prometheus.io/docs/tutorials/getting_started/)
    *   [Beautiful Dashboards with Grafana and Prometheus](https://www.youtube.com/watch?v=fzny5uUaAeY)

### Week 15: Cloud Architecture & Scaling (Stage 11)
*   **Focus**: Virtual architecture boundaries.
*   **Concepts**: Virtual Private Clouds (VPC), IAM users/roles, serverless execution limits, well-architected infrastructure pillars.
*   **Cloud Providers**: AWS, Azure, Google Cloud.
*   **Practical Project**: Build a basic cloud administration scheme: create separate administrative roles, set up a budget threshold alarm, and deploy a secure serverless cloud function.
*   **Resources**:
    *   [Microsoft Azure Fundamentals (AZ-900) Certification Course](https://www.youtube.com/watch?v=NKEFWyqJ5XA)
    *   [AWS Developer by A Cloud Guru](https://acloudguru.com/learning-paths/aws-developer)
    *   [Google Cloud Associate Cloud Engineer Course](https://www.youtube.com/watch?v=jpno8FSqpc8)

### Week 16: SDLC & DevSecOps Fundamentals (Stage 12 & Bonus)
*   **Focus**: High-velocity software practices and shifting security left.
*   **Concepts**: SDLC lifecycle models, Agile Scrum workflows, DevSecOps pipeline boundaries, SAST vs. DAST, Software Supply Chain Security (SLSA).
*   **Tools**: Jira, Trivy, HashiCorp Vault.
*   **Practical Project**: Integrate a security scanning stage using Trivy into your Week 13 CI/CD pipeline to scan your built Docker images for high and critical vulnerabilities.
*   **Resources**:
    *   [What is Scrum? Atlassian Agile Guide](https://www.atlassian.com/agile/scrum)
    *   [OWASP DevSecOps Guideline](https://owasp.org/www-project-devsecops-guideline/)
    *   [Trivy Documentation](https://trivy.dev/latest/)
    *   [Supply Chain Levels for Software Artifacts (SLSA)](https://slsa.dev/)

---

## 📈 Tips for Success
1.  **Strict 2-Hour Daily Blocks**: Treat learning like production uptime. Reserve 2 hours every single day to work through the code examples or build tasks.
2.  **Learn by Breaking**: When practicing with Nginx, Kubernetes, or Docker, deliberately change config files to fail, and then use your monitoring and logging tools to diagnose the failure.
3.  **Document as You Go**: Add your configs, scripts, and notes back to your local repository. This builds your visible engineering portfolio directly as you learn!
