package main

import "github.com/gin-gonic/gin"
import redigo "github.com/garyburd/redigo/redis"
import  "fmt"
var pool *redigo.Pool

func init() {
    redis_host := "wemore-redis.jmg4un.ng.0001.aps1.cache.amazonaws.com"
    redis_port := 6379
    pool_size := 20
    pool = redigo.NewPool(func() (redigo.Conn, error) {
        c, err := redigo.Dial("tcp", fmt.Sprintf("%s:%d", redis_host, redis_port))
        if err != nil {
            return nil, err
        }
        return c, nil
    }, pool_size)
}


func main() {

	gin.SetMode(gin.ReleaseMode)
	r := gin.Default()
	r.GET("/ping", func(c *gin.Context) {
		cc := pool.Get()
		_, err := cc.Do("SET", "go_key", "redigo")
	    	if err != nil {
        		fmt.Println("err while setting:", err)
		}

		c.JSON(200, gin.H{
			"message": "pong",
		})
	})
	r.Run() // listen and serve on 0.0.0.0:8080
}

