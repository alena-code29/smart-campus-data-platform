cube(`StudentRisk`, {
  sql: `SELECT * FROM student_risk_features`,

  measures: {
    studentCount: {
      type: `count`,
      title: `StudentCount`
    },

    avgGrade: {
      sql: `avg_grade`,
      type: `avg`,
      title: `AvgGrade`
    },

    avgAttendanceRate: {
      sql: `attendance_rate`,
      type: `avg`,
      title: `AvgAttendanceRate`
    },

    highRiskStudents: {
      type: `count`,
      filters: [{ sql: `${CUBE}.risk_level = 'high'` }],
      title: `HighRiskStudents`
    },

    avgLmsActivity: {
      sql: `lms_activity_score`,
      type: `avg`,
      title: `AvgLmsActivity`
    }
  },

  dimensions: {
    studentId: {
      sql: `student_id`,
      type: `number`,
      primaryKey: true
    },

    fullName: {
      sql: `full_name`,
      type: `string`
    },

    faculty: {
      sql: `faculty`,
      type: `string`
    },

    groupId: {
      sql: `group_id`,
      type: `string`
    },

    riskLevel: {
      sql: `risk_level`,
      type: `string`
    }
  }
});
