pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                bat 'python -m venv .venv'
                bat '.venv\\Scripts\\python -m pip install --upgrade pip'
                bat '.venv\\Scripts\\pip install -r requirements-dev.txt'
            }
        }

        stage('Run tests') {
            steps {
                bat '.venv\\Scripts\\pytest'
            }
        }

        stage('Run evals') {
            steps {
                bat '.venv\\Scripts\\python -m evals.run_evals'
            }
        }

        stage('Build Docker image') {
            steps {
                bat 'docker build -t ai-incident-agent:latest .'
            }
        }
    }
}