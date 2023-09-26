package main

import (
    "fmt"
    "net/http"
    "io"
    "github.com/gofiber/fiber/v2"
)

func main() {
    app := fiber.New()

    app.Get("/", func(c *fiber.Ctx) error {
        return c.Status(c.Response().StatusCode()).JSON(fiber.Map{"message": "Hello, Golang!"})
    })

    app.Get("/get-token-balance", func(c *fiber.Ctx) error {
        chain := c.Query("chain")
        address := c.Query("address")

        url := fmt.Sprintf("https://deep-index.moralis.io/api/v2.2/%s/balance?chain=%s", address, chain)
    
        req, _ := http.NewRequest("GET", url, nil)
      
        req.Header.Add("Accept", "application/json")
        req.Header.Add("X-API-Key", "KVUjiwZZQHfBN3ttK7lPeSmmWdsAq2yyoDGfB12qkmqpoWrfjwWsH478ewzmk4n3")
      
        res, _ := http.DefaultClient.Do(req)
      
        defer res.Body.Close()
        body, _ := io.ReadAll(res.Body)
      
        fmt.Println(res)
        fmt.Println(string(body))

        return c.Status(c.Response().StatusCode()).JSON(string(body))

    })



    app.Listen(":3000")
}