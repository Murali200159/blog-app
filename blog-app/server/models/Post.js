const mongoose = require('mongoose');

    const postSchema = new mongoose.Schema({
      title: { type: String, required: true, minlength: 1, maxlength: 100 },
      content: { type: String, required: true, minlength: 10 },
      username: { type: String, required: true },
      imageURL: { type: String, match: /^(https?:\/\/.*\.(?:png|jpg|jpeg|gif|webp))$/ },
      createdAt: { type: Date, default: Date.now }
    });

    module.exports = mongoose.model('Post', postSchema);