package main

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"

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

		// fmt.Println(res)
		fmt.Println(string(body))

		var data map[string]interface{}
		err := json.Unmarshal([]byte(body), &data)

		if err != nil {
			return err
		}

		return c.Status(c.Response().StatusCode()).JSON(data)

	})

	app.Get("/get-user-nfts", func(c *fiber.Ctx) error {
		chain := c.Query("chain")
		address := c.Query("address")
		url := fmt.Sprintf("https://deep-index.moralis.io/api/v2.2/%s/nft?chain=%s&format=decimal&media_items=false", address, chain)

		req, _ := http.NewRequest("GET", url, nil)

		req.Header.Add("Accept", "application/json")
		req.Header.Add("X-API-Key", "KVUjiwZZQHfBN3ttK7lPeSmmWdsAq2yyoDGfB12qkmqpoWrfjwWsH478ewzmk4n3")

		res, _ := http.DefaultClient.Do(req)

		defer res.Body.Close()
		body, _ := io.ReadAll(res.Body)

		// fmt.Println(res)
		fmt.Println(string(body))

		var data map[string]interface{}
		err := json.Unmarshal([]byte(body), &data)

		if err != nil {
			return err
		}

		return c.Status(c.Response().StatusCode()).JSON(data)

	})

	app.Listen(":3000")
}
