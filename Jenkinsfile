pipeline{
    agent any
    stages{
        stage("Code Clone"){
            steps{
                git url: "https://github.com/Shreerajp555/two-tier-flask-app.git", branch: "main"
            }
        }
        stage("Build Stage"){
            steps{
                sh "docker build -t two-tier-flask-app:latest ."
            }
        }
        stage("TEST"){
            steps{
                echo "Testing team will do test"
            }
        }
        stage("Push to DockerHub"){
            steps{
                withCredentials([usernamePassword(credentialsId:"dockerHubCreds",
                passwordVariable: "dockerHubPass",
                usernameVariable: "dockerHubUser"
                )]){
                sh "docker login -u ${env.dockerHubUser} -p ${dockerHubPass}"
                sh "docker image tag two-tier-flask-app:latest ${dockerHubUser}/two-tier-flask-app:latest"
                sh "docker push ${env.dockerHubUser}/two-tier-flask-app:latest"
                }
            }
        }
        stage("Deploy"){
            steps{
                sh "docker compose up -d --build flaskapp"
            }
        }
    }
}
