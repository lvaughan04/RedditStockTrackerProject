package com.lvclones.RedditStockTracker.repositories;

import org.bson.types.ObjectId;
import org.springframework.data.mongodb.repository.MongoRepository;
import com.lvclones.RedditStockTracker.models.Stock;

public interface StockRepository extends MongoRepository<Stock, ObjectId>{

}
