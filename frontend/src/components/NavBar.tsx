import { NavLink } from "react-router-dom";
import { HashLink } from "react-router-hash-link";

const NavLinkList = () => {
  return (
    <>
      <NavLink
        to="/home"
        className="text-white/40 hover:text-white/60 focus:text-white"
      >
        Home
      </NavLink>
      <HashLink
        smooth
        to="/home#about"
        className="text-white/40 hover:text-white/60 focus:text-white"
      >
        About Us
      </HashLink>
      <NavLink
        to="/events"
        className="text-white/40 hover:text-white/60 focus:text-white"
      >
        Events
      </NavLink>
      <NavLink
        to="/projects"
        className="text-white/40 hover:text-white/60 focus:text-white"
      >
        Projects
      </NavLink>
      <NavLink
        to="/community"
        className="text-white/40 hover:text-white/60 focus:text-white"
      >
        Community
      </NavLink>
      <NavLink
        to="/dashboard"
        className="text-white/40 hover:text-white/60 focus:text-white"
      >
        Dashboard
      </NavLink>
    </>
  );
};

const NavBar = () => {
  return (
    <div className="sticky top-0 z-100 m-0 py-4 bg-transparent backdrop-blur-lg ">
      <div className="flex items-center justify-between px-14">
        <div className="flex gap-x-2 items-center">
          <img
            src="/vac_tech_jr_logo.jpg"
            alt="logo"
            className="h-10 w-10 object-contain rounded-full"
          />
          <p className="text-xl font-semibold text-white">Vac Tech Jr</p>
        </div>

        <div className="flex items-center gap-14">
          <div className="flex gap-x-14  cursor-pointer">
            <NavLinkList />
          </div>

          <button className="cursor-pointer font-semibold text-primary border-2 object-content rounded-4xl px-4 py-2 border-white text-white hover:bg-white hover:text-[#0a1a33] transition">
            Get Started
          </button>
        </div>
      </div>
    </div>
  );
};

export default NavBar;
