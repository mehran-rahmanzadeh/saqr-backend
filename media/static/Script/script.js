gsap.registerPlugin(ScrollTrigger);

let sections = gsap.utils.toArray(".panel");

gsap.to(sections, {
  xPercent: -100 * (sections.length - 1),
  ease: "none",
  scrollTrigger: {
    trigger: ".container",
    pin: true,
    scrub: 1,
    // base vertical scrolling on how wide the container is so it feels more natural.
    end: "+=3500",
  }
});


const delSections = document.querySelectorAll("#aboutus");

delSections.forEach(section => {
  const containerAnim = gsap.to(section.querySelector("#pointsvg"), {
    y: "40vh",
    ease: "none"
  });
  
  const imageAnim = gsap.to(section.querySelector("svg"), {
    y: "-15vh",
    ease: "none",
    paused: true
  });
  
  const scrub = gsap.to(imageAnim, {
    progress: 1,
    paused: true,
    ease: "power3",
    duration: parseFloat(section.dataset.scrub) || 0.1,
    overwrite: true
  });
  
  ScrollTrigger.create({
    animation: containerAnim,
    scrub: true,
    trigger: section,
    start: "top bottom",
    end: "bottom top",
    onUpdate: self => {
      scrub.vars.progress = self.progress;
      scrub.invalidate().restart();
    }
  });
});


