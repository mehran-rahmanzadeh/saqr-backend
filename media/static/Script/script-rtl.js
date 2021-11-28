gsap.registerPlugin(ScrollTrigger);

let sections = gsap.utils.toArray(".panel");

gsap.set( sections, { xPercent: -100 * (sections.length - 1) })

gsap.to(sections, {
  xPercent: 0,
  ease: "none",
  scrollTrigger: {
    trigger: ".container",
    pin: true,
    scrub: 1,
    // base vertical scrolling on how wide the container is so it feels more natural.
    end: "+=3500"
  }
});