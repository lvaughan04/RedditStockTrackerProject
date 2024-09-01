package com.lvclones.RedditStockTracker.models;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
import org.bson.types.ObjectId;


@Document("SP500")
public record Stock(

    @Id ObjectId id,
    String symbol,
    String security,
    String gicsSector,
    String gicsSubIndustry,
    String headquartersLocation,
    String dateAdded, // make sure to convert to Date "YYYY/MM/DD"
    int cik,
    int founded,
    Post[] posts //array of posts objects in which the posts contain the stock
){}


