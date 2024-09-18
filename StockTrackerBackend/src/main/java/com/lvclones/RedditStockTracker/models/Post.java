package com.lvclones.RedditStockTracker.models;

import org.bson.types.ObjectId;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.data.mongodb.core.mapping.Field;
import java.time.Instant;

@Document("Posts")
public record Post(

    @Id ObjectId id,
    @Field("stock_references") ObjectId[] stockReferences,
    @Field("subreddit")String subreddit,
    @Field("author")String author,
    @Field("body") String body,
    @Field("title") String title,
    @Field("url") String url,
    @Field("timestamp") Instant timestamp
) {}
