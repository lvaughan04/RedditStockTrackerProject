package com.lvclones.RedditStockTracker.repositories;

import org.bson.types.ObjectId;
import org.springframework.data.mongodb.repository.MongoRepository;
import com.lvclones.RedditStockTracker.models.Post;

public interface PostRepository extends MongoRepository<Post, ObjectId>{
    
}
