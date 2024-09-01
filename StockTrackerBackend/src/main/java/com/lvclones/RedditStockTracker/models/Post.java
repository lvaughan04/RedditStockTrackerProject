package com.lvclones.RedditStockTracker.models;

import org.bson.types.ObjectId;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
import java.time.Instant;

@Document("Posts")
public record Post(

    @Id ObjectId id,
    ObjectId[] stockReferences,
    String subreddit,
    String author,
    String body,
    String title,
    String url,
    Instant timestamp
) {}
