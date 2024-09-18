package com.lvclones.RedditStockTracker.services;

import org.springframework.stereotype.Service;
import com.lvclones.RedditStockTracker.repositories.StockRepository;
import org.bson.types.ObjectId;
import java.util.List;
import com.lvclones.RedditStockTracker.models.Stock;

@Service
public class StockService {
    
    private StockRepository stockRepository;

    public StockService(StockRepository stockRepository){
        this.stockRepository = stockRepository;
    }

    public List<Stock> getAllStocks() {
        return stockRepository.findAll();
    }

    public Stock getStockById(ObjectId id){
        return stockRepository.findById(id)
            .orElse(null);
    }

    public Stock getStockBySymbol(String symbol){
        return stockRepository.getStockBySymbol(symbol);
    }
}
