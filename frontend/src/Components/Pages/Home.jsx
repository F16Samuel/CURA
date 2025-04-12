import React from "react";
import { motion } from "framer-motion";
import Navbar from "../Navbar/Navbar";
import Hero from "../Home/hero";
import HowItWorks from "../Home/howitworks";
import Features from "../Home/Features";
import Footer from "../Footer/Footer";

const Home = () => {
  return (
    <div>
      <Navbar/>
      <Hero/>
      <HowItWorks/>
      <Features/>
      <Footer/>
    </div>
  );
};

export default Home;
