const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');

const app = express();
app.use(express.json());
app.use(cors());

const PORT = 3000;

// MongoDB connection
mongoose.connect('mongodb://localhost:27017/dealershipsDB', {
  useNewUrlParser: true,
  useUnifiedTopology: true
}).then(() => console.log('✅ MongoDB connected'))
  .catch(err => console.error('MongoDB error:', err));

// Schemas
const dealerSchema = new mongoose.Schema({
  id: Number,
  full_name: String,
  short_name: String,
  address: String,
  city: String,
  st: String,
  zip: String,
  lat: Number,
  long: Number,
});

const reviewSchema = new mongoose.Schema({
  id: Number,
  dealership: Number,
  name: String,
  purchase: Boolean,
  review: String,
  purchase_date: String,
  car_make: String,
  car_model: String,
  car_year: String,
});

const Dealer = mongoose.model('Dealer', dealerSchema);
const Review = mongoose.model('Review', reviewSchema);

// Seed data
const seedDealers = async () => {
  const count = await Dealer.countDocuments();
  if (count === 0) {
    await Dealer.insertMany([
      { id: 1, full_name: "Midwest Motors", short_name: "midwest", address: "100 Main St", city: "Wichita", st: "Kansas", zip: "67202", lat: 37.69, long: -97.34 },
      { id: 2, full_name: "Sunshine Auto", short_name: "sunshine", address: "200 Oak Ave", city: "Miami", st: "Florida", zip: "33101", lat: 25.77, long: -80.19 },
      { id: 3, full_name: "Golden State Cars", short_name: "golden", address: "300 Elm Blvd", city: "Los Angeles", st: "California", zip: "90001", lat: 34.05, long: -118.24 },
      { id: 4, full_name: "Prairie Dealers", short_name: "prairie", address: "400 Wheat Rd", city: "Topeka", st: "Kansas", zip: "66601", lat: 39.05, long: -95.68 },
      { id: 5, full_name: "Big Apple Auto", short_name: "bigapple", address: "500 Broadway", city: "New York", st: "New York", zip: "10001", lat: 40.71, long: -74.00 },
    ]);
    console.log('✅ Dealers seeded');
  }
};

const seedReviews = async () => {
  const count = await Review.countDocuments();
  if (count === 0) {
    await Review.insertMany([
      { id: 1, dealership: 1, name: "John Smith", purchase: true, review: "Fantastic services and friendly staff!", purchase_date: "2023-06-15", car_make: "Toyota", car_model: "Camry", car_year: "2022" },
      { id: 2, dealership: 1, name: "Jane Doe", purchase: false, review: "Great experience, very professional.", purchase_date: "", car_make: "", car_model: "", car_year: "" },
      { id: 3, dealership: 2, name: "Bob Johnson", purchase: true, review: "Excellent dealership! Loved it.", purchase_date: "2023-07-20", car_make: "Honda", car_model: "Civic", car_year: "2023" },
    ]);
    console.log('✅ Reviews seeded');
  }
};

seedDealers();
seedReviews();

// Task 9 — Get all dealers
app.get('/fetchDealers', async (req, res) => {
  try {
    const { state } = req.query;
    let query = state ? { st: state } : {};
    const dealers = await Dealer.find(query);
    res.json({ dealers });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Task 10 — Get dealer by ID
app.get('/fetchDealer', async (req, res) => {
  try {
    const { id } = req.query;
    const dealers = await Dealer.find({ id: parseInt(id) });
    res.json({ dealers });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Task 8 — Get reviews for dealer
app.get('/fetchReviews', async (req, res) => {
  try {
    const { id } = req.query;
    const reviews = await Review.find({ dealership: parseInt(id) });
    res.json({ reviews });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Post a review
app.post('/postReview', async (req, res) => {
  try {
    const reviewData = req.body.review;
    const count = await Review.countDocuments();
    reviewData.id = count + 1;
    const review = new Review(reviewData);
    await review.save();
    res.json({ message: "Review posted successfully!", review });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.listen(PORT, () => {
  console.log(`✅ Database microservice running on http://localhost:${PORT}`);
});
