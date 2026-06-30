@Library("shared") _
pipeline {
    agent { label "dev" }

    stages {

        stage("Code Clone") {
            steps {
                clone("https://github.com/Shreerajp555/two-tier-flask-app.git", "main")
            }
        }

        stage("Trivy File System Scan") {
            steps {
                trivy_fs()
            }
        }

        stage("Build") {
            steps {
                sh "docker build -t two-tier-flask-app:latest ."
            }
        }

        stage("Test") {
            steps {
                echo "Testing will be done by test team"
            }
        }

        stage("Push to DockerHub") {
            steps {
                docker_push("dockerHubCreds", "two-tier-flask-app")
            }
        }

        stage("Deploy") {
            steps {
                sh "docker compose up -d --build flaskapp"
            }
        }
    }

    post {
        success {
            emailext(
                subject: "Build Successful",
                body: "Good news! Your build was successful.",
                to: 'shreerajpatil29@gmail.com'
            )
        }

        failure {
            emailext(
                subject: "Build Failed",
                body: "Bad news! Your build failed.",
                to: 'shreerajpatil29@gmail.com'
            )
        }
    }
}
