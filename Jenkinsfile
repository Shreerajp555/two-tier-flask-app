pipeline{
    agent {label "dev"}
    stages{
        stage("Code Clone"){
            steps{
                git url: "https://github.com/Shreerajp555/two-tier-flask-app.git", branch: "main"
            }
        }
        stage("filesystem scan"){
            steps{
                sh "trivy fs . -o results.json"
            }
        }
        stage("build"){
            steps{
                sh "docker build -t two-tier-flask-app ."
            }
        }
        stage("Test"){
            steps{
                echo "Tester will test the code"
            }
        }
        stage("Push to Docker Hub"){
            steps{
                withCredentials([usernamePassword(
                    credentialsId: "dockerHubCreds",
                    passwordVariable: "dockerHubPass",
                    usernameVariable: "dockerHubUser")
                    ]){
                        sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPass}"
                        sh "docker image tag two-tier-flask-app ${env.dockerHubUser}/two-tier-flask-app:latest"
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
