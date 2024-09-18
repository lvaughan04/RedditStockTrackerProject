package com.lvclones.RedditStockTracker.models;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.data.mongodb.core.mapping.Field;
import org.bson.types.ObjectId;


@Document("SP500")
public record Stock(


    @Id ObjectId id,
 
    @Field("Symbol") String symbol,
    @Field("Security") String security,
    @Field("GICS Sector") String gicsSector,
    @Field("GICS Sub-Industry") String gicsSubIndustry,
    @Field("Headquarters Location") String headLocation,
    @Field("Date added") String dateAdded, // make sure to convert to Date "YYYY/MM/DD"
    @Field("CIK") String cik,
    @Field("Founded") int founded
){}


