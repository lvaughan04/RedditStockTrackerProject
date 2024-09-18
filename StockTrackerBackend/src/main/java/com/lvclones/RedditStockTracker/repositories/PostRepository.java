package com.lvclones.RedditStockTracker.repositories;

import org.bson.types.ObjectId;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

import com.lvclones.RedditStockTracker.models.Post;
import java.util.List;


public interface PostRepository extends MongoRepository<Post, ObjectId>{

    @Query("{ 'subreddit' : ?0}")
    public List<Post> findPostsBySubreddit(String subreddit);
}
