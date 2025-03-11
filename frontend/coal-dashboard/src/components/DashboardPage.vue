<script>
import API from "../api/api.js";

export default {
  data() {
    return {
      coalData: [],
      newCoal: { name: "", quantity: "", location: "" },
      sortAsc: true,
    };
  },
  async mounted() {
    this.fetchCoalData();
  },
  computed: {
    sortedCoalData() {
      return [...this.coalData].sort((a, b) =>
        this.sortAsc ? a.quantity - b.quantity : b.quantity - a.quantity
      );
    },
  },  
  methods: {
    async fetchCoalData() {
      try {
        const response = await API.get("/coal-data");
        this.coalData = response.data;
      } catch (error) {
        console.error("Error fetching coal data:", error);
      }
    },
    async addCoal() {
      try {
        await API.post("/add-coal", this.newCoal);
        this.fetchCoalData(); // Refresh data after adding
        this.newCoal = { name: "", quantity: "", location: "" }; // Reset form
      } catch (error) {
        console.error("Error adding coal data:", error);
      }
    },
    sortData() {
      this.sortAsc = !this.sortAsc;
    },
  },
};
</script>
