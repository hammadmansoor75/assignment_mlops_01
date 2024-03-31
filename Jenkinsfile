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
            // If you want, you can perform other actions here instead of sending an email
            echo "Pipeline succeeded, Docker image pushed to Docker Hub."
        }
    }
}
