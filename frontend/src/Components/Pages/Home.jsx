import React from "react";
import { motion } from "framer-motion";
import Navbar from "../Navbar/Navbar";
import Hero from "../Home/Hero";
import HowItWorks from "../Home/howitworks";
import Features from "../Home/Features";

const Home = () => {
  return (
    <div>
      <Navbar/>
      <Hero/>
      <HowItWorks/>
      <Features/>
    </div>
  );
};

export default Home;
