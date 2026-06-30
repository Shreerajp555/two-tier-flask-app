@Library("shared") _
pipeline{
    agent {label "dev"}
    stages{
        stage("code clone"){
            steps{
                script{
                    clone("https://github.com/Shreerajp555/two-tier-flask-app.git", branch: "main")
                }
            }
        }
        stage("Trivy File sys Scan"){
            steps{
                script{
                    trivy_fs()
                }
            }
        }
        stage("build"){
            steps{
                sh "docker build -t two-tier-flask-app ."
            }
        }
        stage("test"){
            steps{
                echo "testing will doen by test team"
            }
        }
        stage("Push to DockerHub"){
            steps{
                script{
                    docker_push("dockerHubCreds","two-tier-flask-app")
            }
        }
        stage("deploy"){
            steps{
                sh "docker compose up -d --build flaskapp"
            }
        }
    }
    post{
        success{
            emailext(
                subject: "build successful",
                body: "good news  your build was successful",
                to: 'shreerajpatil29@gmail.com'
                )
        }
        failure{
            emailext(
                subject: "build failed",
                body: "Bad news your build was failed",
                to: 'shreerajpatil29@gmail.com'
                )
        }
    }
}
