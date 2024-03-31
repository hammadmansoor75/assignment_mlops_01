pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                bat "docker login --username hammadmansoor --password hammad0066"
                // Build the Docker image
                bat "docker build -t hammadmansoor/mlops_assignment01:latest ."
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                // Push the image to Docker Hub
                bat "docker push hammadmansoor/mlops_assignment01:latest"
            }
        }
    }

    post {
        success {
            // Email upon successfully completing the pipeline
            mail to: 'i200929@nu.edu.pk',
                 subject: "SUCCESS: Docker image pushed to Docker Hub",
                 body: "The pipeline successfully pushed the Docker image to Docker Hub."
        }
    }
}
