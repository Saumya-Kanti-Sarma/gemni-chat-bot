// server.js
import express from 'express';
import mongoose from 'mongoose';
import dotenv from 'dotenv';

dotenv.config();

const app = express();

// Connect to MongoDB
mongoose.connect(process.env.MONGO_URI)
  .then(() => console.log('MongoDB Connected'))
  .catch(err => console.error('MongoDB connection error:', err));

// Shoe Schema
const shoeSchema = new mongoose.Schema({
  name: String,
  brand: String,
  category: String,
  price: Number
});

const Shoe = mongoose.model('Shoe', shoeSchema);

// GET /shoes?category=...&brand=...&minPrice=...&maxPrice=...&page=...&limit=...
app.get('/shoes', async (req, res) => {
  try {
    const {
      category,
      brand,
      minPrice,
      maxPrice,
      page = 1,
      limit = 7
    } = req.query;

    // Build filter object
    const filter = {};
    if (category) filter.category = category;
    if (brand) filter.brand = brand;
    if (minPrice || maxPrice) {
      filter.price = {};
      if (minPrice) filter.price.$gte = Number(minPrice);
      if (maxPrice) filter.price.$lte = Number(maxPrice);
    }

    // Pagination
    const skip = (Number(page) - 1) * Number(limit);

    const shoes = await Shoe.find(filter)
      .skip(skip)
      .limit(Number(limit));

    const total = await Shoe.countDocuments(filter);

    res.json({
      total,
      page: Number(page),
      limit: Number(limit),
      totalPages: Math.ceil(total / limit),
      data: shoes
    });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Server Error' });
  }
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
