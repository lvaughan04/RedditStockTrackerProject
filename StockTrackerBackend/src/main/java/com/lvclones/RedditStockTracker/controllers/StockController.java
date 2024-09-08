package com.lvclones.RedditStockTracker.controllers;

import org.springframework.data.mongodb.repository.Query;
import org.springframework.graphql.data.method.annotation.Argument;
import org.springframework.graphql.data.method.annotation.QueryMapping;
import org.springframework.graphql.data.method.annotation.SchemaMapping;
import org.springframework.stereotype.Controller;
import com.lvclones.RedditStockTracker.models.Stock;
import java.util.List;
import org.bson.types.ObjectId;

import com.lvclones.RedditStockTracker.services.StockService;

@Controller
public class StockController {

    private StockService stockService;

    public StockController(StockService stockService){
        this.stockService = stockService;
    }

    @QueryMapping
    public List<Stock> getStocks(){
        return stockService.getStocks();
    }

    @QueryMapping
    public Stock getStockById(@Argument String id){
        return stockService.getStockById( new ObjectId(id));
    }

    
}
