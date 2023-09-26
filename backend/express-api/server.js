const express = require('express')
const app = express()
const PORT = 5005

const Moralis = require('moralis').default;
const {EvmChain} = require('@moralisweb3/common-evm-utils')

app.get('/get-token-balance', async (req, res) => {
    chain = EvmChain.SEPOLIA
    address = req.query.address
    console.log(chain + address)
    try {
        await Moralis.start({
          apiKey: "KVUjiwZZQHfBN3ttK7lPeSmmWdsAq2yyoDGfB12qkmqpoWrfjwWsH478ewzmk4n3"
        });
      
        const response = await Moralis.EvmApi.balance.getNativeBalance({
          "chain": chain,
          "address": address
        });
      
        console.log(response.raw);
        return res.json(response.raw)
      } catch (e) {
        console.error(e);
      }
})


app.get('/', (req, res) => {
    res.json({'message': 'Hello, Node!'})
})

app.listen(PORT, () => {
    console.log(`Auxano moralis wallet app running at ${PORT}`)
})